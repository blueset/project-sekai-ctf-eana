import { useCallback, useEffect, useRef, useState } from "react";
import Instance from "./Instance";
import { enqueueSnackbar } from 'notistack'
import ReCAPTCHA from "react-google-recaptcha";

export type InstanceInfo = {
    category: string,
    hidden: boolean,
    id: number,
    lifetime: number,
    name: string,
    running: boolean,
    proto: string,
    host?: string,
    password?: string,
    port?: number,
    remaining?: number,
    // local-only property
    remainingLaunchingPollCount?: number,
};

const mergeInstances = (oldInstances: InstanceInfo[], newInstances: InstanceInfo[]) => {
    const newInstancesMap = new Map(newInstances.map(instance => [instance.id, instance]));
    const mergedInstances = [...oldInstances.map(instance => {
        const newInstance = newInstancesMap.get(instance.id);
        if (newInstance) {
            if (newInstance.running) return newInstance;
            else return { ...instance, ...newInstance };
        } else {
            return instance;
        }
    }), ...newInstances.filter(instance => !oldInstances.find(oldInstance => oldInstance.id === instance.id))];
    return mergedInstances;
}

export default function Instances() {
    const [instances, setInstances] = useState<InstanceInfo[]>([]);
    const isFetchingRef = useRef(false);
    const recaptchaRef = useRef<ReCAPTCHA>(null);
    useEffect(() => {
        function refetch() {
            if (isFetchingRef.current) return;
            isFetchingRef.current = true;
            fetch("/challenges").then((res) => res.json()).then((json) => {
                setInstances((insts) => mergeInstances(insts, json.challenges));
            }).finally(() => { isFetchingRef.current = false; });
        }
        const interval = setInterval(() => {
            setInstances(instances => {
                let needRefetch = false;
                const newInstances = [...instances.map(instance => {
                    const newInstance = { ...instance };
                    if (newInstance.running && newInstance.remaining) {
                        newInstance.remaining--;
                        if (newInstance.remaining <= 0) {
                            newInstance.running = false;
                            needRefetch = true;
                        }
                    } else if (newInstance.remainingLaunchingPollCount) {
                        newInstance.remainingLaunchingPollCount--;
                        needRefetch = true;
                        if (newInstance.remainingLaunchingPollCount <= 0) {
                            // exceeded max poll count, reload page
                            newInstance.remainingLaunchingPollCount = undefined;
                            window.location.reload();
                        }
                    }
                    return newInstance;
                })];
                if (needRefetch) {
                    refetch();
                }
                return newInstances;
            });
        }, 1000);
        refetch();
        return () => clearInterval(interval);
    }, [setInstances]);

    const launchInstance = useCallback((instance: InstanceInfo) => async () => {
        const challenge_id = instance.id;
        const token = recaptchaRef.current?.getValue();
        try {
            const response = await fetch("/launcher", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    'challenge_id': challenge_id,
                    'g-recaptcha-response': token
                }),
            });

            const data = await response.json();
            if (data.success) {
                setInstances(instances =>
                    instances.map(instance => {
                        if (instance.id === challenge_id) {
                            return {
                                ...instance,
                                remainingLaunchingPollCount: 10,
                            };
                        } else {
                            return instance;
                        }
                    })
                );
                enqueueSnackbar(data.msg, { variant: "success" });
            } else {
                enqueueSnackbar(data.msg, { variant: "error" });
            }
        } catch (e) { }
    }, []);

    return (<div>
        {instances.map((instance) => <Instance key={instance.id} instance={instance} launch={launchInstance(instance)} />)}
        <ReCAPTCHA ref={recaptchaRef} sitekey="6LcfunchAAAAACqWkEiNSjpisc4A4bihYdj2fRIC" />
    </div>);
}