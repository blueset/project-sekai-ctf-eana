import { Icon } from '@iconify/react';
import { useCallback, useRef } from 'react';
import tippy from 'tippy.js';

export default function CopyableLabel({ value }: { value: string }) {
  const buttonRef = useRef<HTMLButtonElement>(null);

  const onClick = useCallback(() => {
    const button = buttonRef.current;
    if (!button) return;
    const tooltip = tippy(button, {
      content: navigator.clipboard === undefined ? "Clipboard is not available." : "Copied!",
      trigger: "manual",
      theme: "lunaDefault",
      appendTo: "parent",
      arrow: false,
    });
  
    const showTooltip = () => {
      tooltip.show();
      setTimeout(() => {
        tooltip.hide();
        tooltip.destroy();
      }, 1500);
    };
  
    if (navigator.clipboard === undefined) showTooltip();
    else navigator.clipboard.writeText(value).then(showTooltip);
  }, [buttonRef]);
  
  return (
    <div className="inputFrame copyableConnection">
      {value.startsWith("http") ?
        <code className="connectionValue"><a href={value} target="_blank">{value}</a></code>
        :
        <code className="connectionValue">{value}</code>
      }
      <button className="inputIcon" type="button" ref={buttonRef} onClick={onClick}>
        <Icon icon="material-symbols:content-copy" />
      </button>
    </div>
  );
}