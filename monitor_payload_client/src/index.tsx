import * as React from "react";
import * as ReactDOM from "react-dom";

import { Sample } from "./components/Sample";

ReactDOM.render(
    <Sample compiler="TypeScript" framework="React" />,
    document.getElementById( "app" )
);