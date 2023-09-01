const totalDuration = 300;

export default function Countdown({ time }: { time: number }) {
    const label = `${Math.floor(time / 60)}:${(time % 60).toString().padStart(2, '0')} remaining`;
    return (
        <div className="countdown" style={{
            // @ts-ignore
            "--progress-percentage": `${(1 - time / totalDuration) * 100}%`,
        }}>
            <div className="back">{label}</div>
            <div className="front" aria-hidden>{label}</div>
        </div>
    );
}