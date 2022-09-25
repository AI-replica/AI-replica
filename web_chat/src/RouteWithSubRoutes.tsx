// A special wrapper for <Route> that knows how to
// handle "sub"-routes by passing them in a `routes`

import { Route } from "react-router-dom";

// prop to the component it renders.
// for the example, check https://v5.reactrouter.com/web/example/route-config
function RouteWithSubRoutes(route: any) {
    return (
      <Route
        path={route.path}
        // render={(props: any) => (
        //   // pass the sub-routes down to keep nesting
        //   <route.component {...props} routes={route.routes} />
        // )}
      />
    );
  }
  