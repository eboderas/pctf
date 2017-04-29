import * as React from "react";

import { DSTHistogram, HistogramProps } from "./DSTHistogram"
import { PayloadHistogram } from "./PayloadHistogram"
import { Results } from "./Results"
import axios = require( 'axios' );

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

const payloadHistProps: HistogramProps = {
    chartType: "Histogram",
    data: [
    ["Destination Port", "Frequency"],
    ["249", 8],
    ["125", 93],
    ["169", 105],
    ["285", 50],
    ["102", 14],
    ["181", 3],
    ["145", 56],
    ["221", 1],
    ["147", 24],
    ["299", 1],
    ["119", 52],
    ["216", 147],
    ["206", 53],
    ["143", 80],
    ["256", 2],
    ["177", 12],
    ["277", 77],
    ["179", 62],
    ["254", 111],
    ["135", 96],
    ["182", 50],
    ["205", 148],
    ["140", 3],
    ["289", 73],
    ["161", 25],
    ["111", 25],
    ["219", 2],
    [107, 150]
    ],
    options:{
        "title": "Frequency of Payload Length",
        "histogram": {
            maxNumBuckets: 40
        }
    },
    width: "100%"
 }

export class App extends React.Component<undefined, undefined> {
    state: any;
    constructor( props: any ){
        super( props );
        this.state = {
            results: [ 'Select Port or Payload Length to view data' ]
        };

        axios.post( '/main' )
            .then( ( response: any ) => {
                console.log( 'Response: ', response );
            } )
            .catch( ( error: any ) => {
                console.log( 'Error: ', error );
            } );
    }
    render() {
        return(
            <div>
                <DSTHistogram chartType={ dstHistProps.chartType } data={ dstHistProps.data } options={ dstHistProps.options } width={ dstHistProps.width } results={ this.state.results } update={ this.update.bind( this ) } />
                <PayloadHistogram chartType={ payloadHistProps.chartType } data={ payloadHistProps.data } options={ payloadHistProps.options } width={ payloadHistProps.width } results={ this.state.results } update={ this.update.bind( this ) } />
                <Results results={ this.state.results } />
            </div> 
        );
    }
    update( data: any ): void{
        console.log( 'Parent Data :', data );
        // console.log( 'state :', {this.state} );
        this.setState({
            results: [ data[0] ]
        });
    }
}