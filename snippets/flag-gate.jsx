export const FlagGate = ({ flag, children, fallback = null }) => {
  const [isOn, setIsOn] = useState(null);

  useEffect(() => {
    let cancelled = false;

    const evaluate = () => {
      window.ldClient.waitUntilReady().then(() => {
        if (!cancelled) setIsOn(window.ldClient.variation(flag, false));
      });
    };

    if (window.ldClient) {
      evaluate();
    } else {
      // ld-init.js runs after hydration, so the client may not exist yet.
      const onReady = () => evaluate();
      window.addEventListener('ld-ready', onReady);
      return () => {
        cancelled = true;
        window.removeEventListener('ld-ready', onReady);
      };
    }

    return () => {
      cancelled = true;
    };
  }, [flag]);

  // Render nothing until the flag is evaluated, so there is no flash of the wrong content.
  if (isOn === null) return null;
  return isOn ? children : fallback;
};
