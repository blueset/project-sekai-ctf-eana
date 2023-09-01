import { ReactNode } from "react";
import { Icon } from '@iconify/react';

export function Info({ children }: { children: ReactNode }) {
    return (
        <div className="info" role="alert">
            <Icon icon="material-symbols:info" />
            <div className="infoDetails">{children}</div>
        </div>
    );
}