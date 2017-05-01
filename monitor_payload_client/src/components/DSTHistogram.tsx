import * as React from "react";
import { render } from 'react-dom';
import { Chart } from 'react-google-charts';
import * as axios from 'axios';

export interface HistogramProps {
	chartType: string;
	data: Array<any>;
	options?: any;
	width?: string;
	chartEvents?: any;
	results?: any;
	update? : any;
}

export class DSTHistogram extends React.Component <HistogramProps, undefined> {
	chartEvents: any;
	data: any;
	constructor(props: any){
		super(props);
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

            const dbResults: Array<any> = [ ["Destination Port", "Frequency"] ];
            response.data.db.forEach( ( row: any ) => {
                dbResults.push([ row.dst_port.toString(), row.count ]);
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
			graph_id="dst-histogram"
			width={this.props.width}
			height="400px"
			legend_toggle
			chartEvents={this.chartEvents}
			/>
		</div>
		);
	}
}