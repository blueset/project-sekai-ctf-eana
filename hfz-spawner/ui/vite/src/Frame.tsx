import { ReactNode, useEffect, useRef } from "react";
import { Icon } from '@iconify/react';
import iconWallImg from './assets/images/icon-wall.svg';
import Menu from "./Menu";

const BackgroundCanvasResources: {
    canvas?: HTMLCanvasElement,
    offscreenCanvas?: HTMLCanvasElement,
} = {};

const rad50 = 0.872665;
const rad40 = Math.PI / 2 - rad50;
const scale = 0.5;

function buildIconWallData(w: number, h: number, iconWall: HTMLImageElement) {
    const offscreenCanvas = document.createElement("canvas");
    const offscreenCtx = offscreenCanvas.getContext("2d");
    if (!offscreenCtx) return;

    const a1 = w * Math.cos(rad40),
        a2 = h * Math.cos(rad50),
        b1 = h * Math.cos(rad40),
        b2 = w * Math.cos(rad50);

    const width = (b1 + b2) / scale;
    const height = (a1 + a2 + 580) / scale;

    offscreenCanvas.width = width;
    offscreenCanvas.height = height;

    const pattern = offscreenCtx.createPattern(iconWall, "repeat");
    if (!pattern) return;
    offscreenCtx.fillStyle = pattern;
    offscreenCtx.fillRect(0, 0, width, height);
    BackgroundCanvasResources.offscreenCanvas = offscreenCanvas;
}

function drawPatternScale(ctx: CanvasRenderingContext2D, offscreenCanvas: HTMLCanvasElement, startx: number, starty: number, width: number, height: number) {
    ctx.scale(scale, scale);
    ctx.drawImage(offscreenCanvas, startx / scale, starty / scale, width / scale, height / scale);
    ctx.restore();
}

function render(timer: number) {
    timer = (timer / 30) % 580;
    const { canvas, offscreenCanvas } = BackgroundCanvasResources;
    if (canvas && offscreenCanvas) {
        const ctx = canvas.getContext("2d");
        if (!ctx) return;
        ctx.save();
        const w = canvas.width,
            h = canvas.height;
        ctx.clearRect(0, 0, w, h);
        ctx.save();
        ctx.rotate(rad50);
        const a1 = w * Math.cos(rad40),
            a2 = h * Math.cos(rad50),
            b1 = h * Math.cos(rad40),
            b2 = w * Math.cos(rad50);
        ctx.translate(0, -timer);
        drawPatternScale(ctx, offscreenCanvas, 0, -a1, b1 + b2, a1 + a2 + 580);
    }
}

function frame(timer: number) {
    render(timer);
    return window.requestAnimationFrame(frame);
}

function IconWallCanvasInit(canvas: HTMLCanvasElement) {
    const container = document.querySelector(".triangleContainer");
    if (!container || container.classList.contains("page-challenges-listing")) {
        return;
    }

    const iconWall = new Image();
    iconWall.crossOrigin = "anonymous";
    iconWall.onload = () => {
        buildIconWallData(canvas.width, canvas.height, iconWall);
    };
    iconWall.src = iconWallImg;

    BackgroundCanvasResources.canvas = canvas;

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    window.addEventListener("resize", () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        buildIconWallData(canvas.width, canvas.height, iconWall);
    });

    window.requestAnimationFrame(frame);
}

export default function Frame({ title, subtitle, children }: { title: string, subtitle: string, children: ReactNode }) {
    const canvasRef = useRef<HTMLCanvasElement>(null);

    useEffect(() => {
        if (canvasRef.current) {
            IconWallCanvasInit(canvasRef.current);
        }
    }, []);

    return (
        <div className="triangleContainer">
            <canvas ref={canvasRef} id="iconWallCanvas" className="iconWallCanvas" />
            <div className="controlRow">
                <div className="titleContainer">
                    <button className="button iconButton" id="backButton" aria-label="Go back" title="Go back" onClick={() => {
                        if (window.history.length > 1) window.history.back();
                        else window.location.href = "/";
                    }}>
                        <Icon icon="icon-park-solid:back" />
                    </button>
                    <div className="titleGroup">
                        <h1 className="title">{title}</h1>
                        <h2 className="subtitle"><span>{subtitle}</span></h2>
                    </div>
                </div>
                <div className="filler"></div>
                <Menu />
            </div>
            <div className="contentWrapper">
                {children}
            </div>
        </div>
    );
}