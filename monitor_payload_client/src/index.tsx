import * as React from "react";
import * as ReactDOM from "react-dom";

import { App } from "./components/App";
import { DSTHistogram, HistogramProps } from "./components/DSTHistogram"

const dstHistProps: HistogramProps = {
    chartType: "Histogram",
    data: [
    ["Destination Port", "Frequency"],
    ["22510", 40],
    ["16471", 23],
    ["46738", 24],
    ["21510", 60],
    ["54688", 35],
    ["50747", 55],
    ["24747", 79],
    ["10102", 4],
    ["49691", 37],
    ["46632", 9],
    ["16615", 15],
    ["2442", 95],
    ["3224", 26],
    ["40612", 44],
    ["12696", 78],
    ["59227", 30],
    ["21625", 26],
    ["9560", 30],
    ["63763", 95],
    ["51852", 9],
    ["35315", 54],
    ["42486", 99],
    ["58431", 13],
    ["7441", 48],
    ["5580", 12],
    ["11012", 73],
    ["39761", 11],
    ["49535", 14]
    ],
    options:{
        "title": "Frequency of ports used",
        "histogram": {
            maxNumBuckets: 20
        }
    },
    width: "100%"
}

// ReactDOM.render(
//     <App compiler="TypeScript" framework="React" />,
//     document.getElementById( "app" )
// );
ReactDOM.render(
    <DSTHistogram chartType={dstHistProps.chartType} data={dstHistProps.data} options={dstHistProps.options} width={dstHistProps.width} />,
    document.getElementById( 'app' )
);