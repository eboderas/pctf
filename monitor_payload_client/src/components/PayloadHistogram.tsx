import * as React from "react";
import { render } from 'react-dom';
import { Chart } from 'react-google-charts';
import { HistogramProps } from './DSTHistogram';

export class PayloadHistogram extends React.Component <HistogramProps, undefined> {
	chartEvents: any;
	data: any;
	constructor(props: any){
		super(props);
		// this.data = this.props.data;
		this.chartEvents = [
		{
			eventName: 'select',
			callback(Chart: any) {
				// Returns Chart so you can access props and  the ChartWrapper object from chart.wrapper
				let selectedItem = Chart.chart.getSelection()[0];
				console.log( 'Selected ', selectedItem );
				console.log( 'Data :', props.data[ selectedItem.row + 1 ] );
				// console.log('Data :', this.data.getValue(selectedItem.row, selectedItem.column));
				// props.results.push( props.data[ selectedItem.row + 1 ] );
				// console.log(  )
				props.update( props.data[ selectedItem.row + 1 ] );
			},
		}];
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