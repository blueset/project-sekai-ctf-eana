import React, { useCallback, useEffect, useState } from 'react';
import { Icon } from '@iconify/react';
import dialogPolyfill from 'dialog-polyfill';

export default function Menu() {
    const [isHiding, setIsHiding] = useState(false);
    const dialogRef = React.createRef<HTMLDialogElement>();

    useEffect(() => {
        if (dialogRef.current) {
            dialogPolyfill.registerDialog(dialogRef.current);
        }
    }, []);
    const hideModal = useCallback(() => {
        const modalNode = dialogRef.current;
        if (!modalNode) return;

        const modalHideAnimationEndCallback = () => {
            setIsHiding(false);
            modalNode.close();
            modalNode.removeEventListener('webkitAnimationEnd', modalHideAnimationEndCallback, false);
        }

        setIsHiding(true);
        modalNode.addEventListener('webkitAnimationEnd', modalHideAnimationEndCallback, false);

    }, [dialogRef]);

    const modalClick = useCallback((e: React.MouseEvent<HTMLDialogElement, MouseEvent>) => {
        const modalNode = dialogRef.current;
        if (!modalNode) return;
        var rect = modalNode.getBoundingClientRect();
        var minX = rect.left + modalNode.clientLeft;
        var minY = rect.top + modalNode.clientTop;
        if (e.clientX !== 0 && e.clientY !== 0 &&
            ((e.clientX < minX || e.clientX >= minX + modalNode.clientWidth) ||
                (e.clientY < minY || e.clientY >= minY + modalNode.clientHeight))) {
            hideModal();
        }
    }, []);

    return (
        <>
            <button className="button shade iconButton menuButton buttonNotification" id="mainMenuButton" aria-label="Main menu" title="Main Menu" onClick={() => dialogRef.current?.showModal()}>
                <Icon icon="ic:baseline-menu" />
            </button>
            <dialog className={`modal fit${isHiding ? ' hide' : ''}`} id="mainMenuModal" ref={dialogRef} onClick={modalClick}>
                <h2 className="modalHeader">Menu</h2>
                <div className="modalBody">
                    <a className="button textButton shade primaryIcon" href="/rules">
                        <Icon icon="ic:baseline-contact-page" />
                        <span>Rules</span>
                    </a>

                    <a className="button textButton shade primaryIcon" href="/teams">
                        <Icon icon="ic:baseline-people-alt" />
                        <span>Teams</span>
                    </a>

                    <a className="button textButton shade primaryIcon" href="/users">
                        <Icon icon="ic:baseline-person" />
                        <span>Users</span>
                    </a>
                    <a className="button textButton shade primaryIcon" href="/scoreboard">
                        <Icon icon="mdi:podium" />
                        <span>Ranking</span>
                    </a>

                    <a className="button textButton alternate" href="/">
                        <Icon icon="ic:baseline-home" />
                        <span>Home</span>
                    </a>

                    <a className="button textButton alternate" id="mainMenuTitleBtn" href="/" onClick={() => window.localStorage.setItem("luna_showTitleScreen", "true")}>
                        <Icon icon="icon-park-solid:back" />
                        <span>Title</span>
                    </a>

                    <a className="button textButton alternate" href="/challenges">
                        <Icon icon="fluent:music-note-2-24-filled" />
                        <span>Challenges</span>
                    </a>
                    <a className="button textButton alternate buttonNotification" id="mainMenuTitleBtn" href="/notifications">
                        <Icon icon="ic:baseline-notifications" />
                        <span>Notifications</span>
                    </a>

                    <a className="button textButton small" id="mainMenuTitleBtn" href="/team">
                        <Icon icon="mdi:account-multiple-check" />
                        <span>Your team</span>
                    </a>


                    <a className="button textButton small" id="mainMenuTitleBtn" href="/user">
                        <Icon icon="mdi:account-check" />
                        <span>Profile</span>
                    </a>
                    <a className="button textButton small" id="mainMenuTitleBtn" href="/settings">
                        <Icon icon="mdi:cog" />
                        <span>Settings</span>
                    </a>
                    <a className="button textButton small" id="mainMenuTitleBtn" href="/logout">
                        <Icon icon="mdi:logout-variant" />
                        <span>Log out</span>
                    </a>
                </div>
                <div className="modalFooter">
                    <button className="button textButton shade" id="mainMenuClose" onClick={() => hideModal()}>
                        <span>Close</span>
                    </button>
                </div>
            </dialog>
        </>
    );
}