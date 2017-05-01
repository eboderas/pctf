import * as React from "react";
import { render } from 'react-dom';
import { Chart } from 'react-google-charts';
import { HistogramProps } from './DSTHistogram';

import * as axios from 'axios';
// http://stackoverflow.com/questions/27192621/reactjs-async-rendering-of-components
export class PayloadHistogram extends React.Component <HistogramProps, undefined> {
	chartEvents: any;
	state: any;
	data: any;
	constructor(props: any){
		super(props);
	}
	render() {
		if ( this.state && this.state.data ) {
			return (
				<div className={'my-pretty-chart-container'}>
					<Chart
					chartType={this.props.chartType}
					data={this.state.data}
					options={this.props.options}
					graph_id="payload-histogram"
					width={this.props.width}
					height="400px"
					legend_toggle
					chartEvents={this.state.eventHandler}
					/>
				</div>
			);
		}
		return <div>Loading...</div>;
		
	}
	/**
	 * 1) Make AJAX call and load data
	 * 2) In Promise use data to load state
	 * 3) State change loads new data and re-renders component
	 * @memberof PayloadHistogram
	 */
	componentDidMount(){
		const self = this;
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
			self.data = dbResults;
			self.chartEvents = [
			{
				eventName: 'select',
				callback(Chart: any) {
					let selectedItem = Chart.chart.getSelection()[0];
					console.log( 'Selected ', selectedItem );
					console.log( 'Data :', dbResults[ selectedItem.row + 1 ] );
					self.props.update( dbResults[ selectedItem.row + 1 ] );
				}
			}];
			self.setState({
				data: dbResults,
				eventHandler: self.chartEvents
			});
        }).catch( ( error: any ) => {
            console.log( 'Request Error: ', error );
        });
	}
}