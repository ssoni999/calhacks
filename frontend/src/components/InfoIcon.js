import React, { useState, useRef, useEffect } from 'react';

function InfoIcon({ definition }) {
  const [showTooltip, setShowTooltip] = useState(false);
  const iconRef = useRef(null);
  const tooltipRef = useRef(null);

  useEffect(() => {
    if (showTooltip && iconRef.current && tooltipRef.current) {
      const updatePosition = () => {
        if (iconRef.current && tooltipRef.current && showTooltip) {
          const iconRect = iconRef.current.getBoundingClientRect();
          const tooltip = tooltipRef.current;
          const tooltipHeight = tooltip.offsetHeight || 100; // fallback height
          
          // Position tooltip above the icon, centered
          let topPos = iconRect.top - tooltipHeight - 12;
          
          // If tooltip would go off-screen at top, position it below instead
          if (topPos < 10) {
            topPos = iconRect.bottom + 12;
          }
          
          tooltip.style.position = 'fixed';
          tooltip.style.top = `${topPos}px`;
          tooltip.style.left = `${iconRect.left + iconRect.width / 2}px`;
          tooltip.style.transform = 'translateX(-50%)';
        }
      };
      
      // Use requestAnimationFrame to ensure DOM is updated
      requestAnimationFrame(() => {
        updatePosition();
        // Update again after a short delay to ensure correct height
        setTimeout(updatePosition, 10);
      });
    }
  }, [showTooltip]);

  const handleMouseEnter = () => {
    setShowTooltip(true);
  };

  const handleMouseLeave = () => {
    setShowTooltip(false);
  };

  return (
    <>
      <span
        ref={iconRef}
        className="info-icon"
        onMouseEnter={handleMouseEnter}
        onMouseLeave={handleMouseLeave}
      >
        ⓘ
      </span>
      {showTooltip && (
        <div
          ref={tooltipRef}
          onMouseEnter={handleMouseEnter}
          onMouseLeave={handleMouseLeave}
          className="info-tooltip"
        >
          {definition}
          <div className="info-tooltip-arrow" />
        </div>
      )}
    </>
  );
}

export default InfoIcon;

