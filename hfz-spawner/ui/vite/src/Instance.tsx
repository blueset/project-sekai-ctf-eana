import type { InstanceInfo } from "./Instances";
import webLogo from "./assets/images/Web.svg";
import miscLogo from "./assets/images/Misc.svg";
import cryptoLogo from "./assets/images/Crypto.svg";
import pwnLogo from "./assets/images/Pwn.svg";
import reverseLogo from "./assets/images/Reverse.svg";
import ppcLogo from "./assets/images/PPC.png";
import forensicsLogo from "./assets/images/Forensics.svg";
import CopyableLabel from "./CopyableLabel";
import Countdown from "./Countdown";

const categories = {
    "Misc": miscLogo,
    "Cryptography": cryptoLogo,
    "Forensics": forensicsLogo,
    "Reverse": reverseLogo,
    "Pwn": pwnLogo,
    "PPC": ppcLogo,
    "Web": webLogo,
} as const;

export default function Instance({ instance, launch }: { instance: InstanceInfo, launch: () => void }) {
    return (
        <div className="listItem instanceItem">
            <div className="listItemNumber">
                {instance.category in categories ? <img src={categories[(instance.category as keyof typeof categories)]} alt={instance.category} title={instance.category} className="instanceLogo" /> : instance.category}
            </div>
            <div className="listItemDetails">
                <div className="instanceName">
                    {instance.name}
                    <span className="instanceProto">{instance.proto}</span>
                </div>
                {instance.running ? <div className="instanceInfo">
                    URL <CopyableLabel value={`${instance.proto}://${instance.host}:${instance.port}`} />
                    {instance.password && <>Password <CopyableLabel value={instance.password} /></>}
                    Time <Countdown time={instance?.remaining ?? 0} />
                </div> : <div className="instanceInfo warning">Not running.</div>}
            </div>
            {!instance.running && <div className="listItemScore">
                <button className="button small textButton" onClick={launch} disabled={!!instance.remainingLaunchingPollCount}>
                    <span>{instance.remainingLaunchingPollCount ? "Launching…" : "Launch"}</span>
                </button>
            </div>}
        </div>
    )
}