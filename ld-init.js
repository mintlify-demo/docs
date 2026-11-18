// Loads the LaunchDarkly JS client SDK and initializes it.
// Mintlify includes every .js file in the content directory on every page,
// after the page becomes interactive.
//
// Replace LD_CLIENT_SIDE_ID with your environment's client-side ID
// (LD dashboard -> Account settings -> Projects -> environment -> Client-side ID).
// The client-side ID is public by design; never put an SDK key (sdk-...) or
// API token (api-...) here.
(function () {
  var LD_CLIENT_SIDE_ID = '6afdfcced96bdf0778ce61ad';

  // Do nothing if no client-side ID is set (keeps other pages quiet).
  if (!LD_CLIENT_SIDE_ID) return;
  if (window.ldClient || window.__ldLoading) return;
  window.__ldLoading = true;

  var script = document.createElement('script');
  script.src = 'https://unpkg.com/launchdarkly-js-client-sdk@3/dist/ldclient.min.js';
  script.onload = function () {
    window.ldClient = LDClient.initialize(LD_CLIENT_SIDE_ID, {
      kind: 'user',
      anonymous: true,
    });
    window.ldClient.waitUntilReady().then(function () {
      // Lets components know flags are ready without polling.
      window.dispatchEvent(new Event('ld-ready'));
    });
  };
  document.head.appendChild(script);
})();
