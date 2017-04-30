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
    ["20001", 95],
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
    ["Payload Length", "Frequency"],
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
    ["187", 148],
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
    /**
     * Creates an instance of App and fetches data for rendering,
     * fallback to template data
     * @param {*} props 
     * @memberof App
     */
    constructor( props: any ){
        super( props );
        this.state = {
            type: "initDST",
            results: [ 'Select Port or Payload Length to view data' ],
            meta: "",
            dataDST: dstHistProps.data,
            dataPayload: payloadHistProps.data
        };
        /**
         * Fetching the DST data here
         */
        axios({
            method: 'post',
            url: 'https://pctf.herokuapp.com/main',
            data: {
                type: "initDST"
            }
        }).then( ( response: any ) => {
            console.log( 'Response: ', response );

            const dbResults: Array<any> = [ ["Destination Port", "Frequency"] ];
            response.data.db.forEach( ( row: any ) => {
                dbResults.push([ row.dst_port.toString(), row.count ]);
            });

            console.log( 'DB Results: ', dbResults );
            
            this.setState({
                type: "dst",
                results: this.state.results,
                meta: this.state.meta,
                dataDST: dbResults,
                dataPayload: this.state.dataPayload
            });

        }).catch( ( error: any ) => {
            console.log( 'Request Error: ', error );
        });
        /**
         * Fetching Payload data and rendering
         */
        axios({
            method: 'post',
            url: 'https://pctf.herokuapp.com/main',
            data: {
                type: "initPayload"
            }
        }).then( ( response: any ) => {
            console.log( 'Response: ', response );

            const dbResults: Array<any> = [ ["Payload Length", "Frequency"] ];
            response.data.db.forEach( ( row: any ) => {
                dbResults.push([ row.length.toString(), row.count ]);
            });

            console.log( 'DB Results: ', dbResults );

            this.setState({
                type: "dst",
                results: this.state.results,
                meta: this.state.meta,
                dataDST: this.state.dataDST,
                dataPayload: dbResults
            });

        }).catch( ( error: any ) => {
            console.log( 'Request Error: ', error );
        });
    }
    /**
     * Render React App
     * @returns 
     * @memberof App
     */
    render() {
        return(
            <div>
                <DSTHistogram chartType={ dstHistProps.chartType } data={ this.state.dataDST } options={ dstHistProps.options } width={ dstHistProps.width } results={ this.state.results } update={ this.updateDST.bind( this ) } />
                <PayloadHistogram chartType={ payloadHistProps.chartType } data={ this.state.dataPayload } options={ payloadHistProps.options } width={ payloadHistProps.width } results={ this.state.results } update={ this.updatePayload.bind( this ) } />
                <Results results={ this.state.results } title={ this.state.type } value={ this.state.meta } />
            </div> 
        );
    }
    updateDST( data: any ): void{
        console.log( 'Parent Data :', data );
        // console.log( 'state :', {this.state} );
        this.setState({
            type: "dst",
            results: [ data[0] ],
            meta: data[0],
            dataDST: this.state.dataDST,
            dataPayload: this.state.dataPayload
        });

        axios({
            method: 'post',
            url: 'https://pctf.herokuapp.com/dst',
            data: {
                type: "dst",
                results: this.state.results
            }
        }).then( ( response: any ) => {
            console.log( 'Response: ', response );

            const dbResults: Array<any> = [];
            response.data.db.forEach( ( row: any ) => {
                dbResults.push(row.payload);
            });

            console.log( 'DB Results: ', dbResults );

            this.setState({
                type: "dst",
                results: dbResults,
                meta: response.data.db[0].dst_port,
                dataDST: this.state.dataDST,
                dataPayload: this.state.dataPayload
            });

        } ).catch( ( error: any ) => {
            console.log( 'Request Error: ', error );
        } );
    }
    updatePayload( data: any ): void{
        console.log( 'Parent Data :', data );
        // console.log( 'state :', {this.state} );
        this.setState({
            type: "payload",
            results: [ data[0] ],
            meta: data[0],
            dataDST: this.state.dataDST,
            dataPayload: this.state.dataPayload
        });

        axios({
            method: 'post',
            url: 'https://pctf.herokuapp.com/payload',
            data: {
                type: "payload",
                results: this.state.results
            }
        }).then( ( response: any ) => {
            console.log( 'Response: ', response );

            const dbResults: Array<any> = [];
            response.data.db.forEach( ( row: any ) => {
                dbResults.push(row.payload);
            });

            console.log( 'DB Results: ', dbResults );

            this.setState({
                type: "payload",
                results: dbResults,
                meta: response.data.db[0].length,
                dataDST: this.state.dataDST,
                dataPayload: this.state.dataPayload
            });

        } ).catch( ( error: any ) => {
            console.log( 'Request Error: ', error );
        } );
    }
}