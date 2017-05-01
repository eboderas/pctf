import * as React from "react";
import { render } from 'react-dom';
import { Chart } from 'react-google-charts';
import { HistogramProps } from './DSTHistogram';

import * as axios from 'axios';

export class PayloadHistogram extends React.Component <HistogramProps, undefined> {
	chartEvents: any;
	data: any;
	constructor(props: any){
		super(props);

		/**
         * Friggin chartEvents wont update
		 * Hence the hack
         */
        axios({
            method: 'post',
            url: 'https://pctf.herokuapp.com/main',
            data: {
                type: "initPayload"
            }
        }).then( ( response: any ) => {
            const dbResults: Array<any> = [ ["Payload Length", "Frequency"] ];
            response.data.db.forEach( ( row: any ) => {
                dbResults.push([ row.length.toString(), row.count ]);
            });
			this.data = dbResults;
			this.chartEvents = [
			{
				eventName: 'select',
				callback(Chart: any) {
					let selectedItem = Chart.chart.getSelection()[0];
					console.log( 'Selected ', selectedItem );
					console.log( 'Data :', dbResults[ selectedItem.row + 1 ] );
					props.update( dbResults[ selectedItem.row + 1 ] );
				}
			}];

        }).catch( ( error: any ) => {
            console.log( 'Request Error: ', error );
        });
	}
	render() {
		return (
			<div className={'my-pretty-chart-container'}>
				<Chart
				chartType={this.props.chartType}
				data={this.props.data}
				options={this.props.options}
				graph_id="payload-histogram"
				width={this.props.width}
				height="400px"
				legend_toggle
				chartEvents={this.chartEvents}
				/>
			</div>
		);
	}
}