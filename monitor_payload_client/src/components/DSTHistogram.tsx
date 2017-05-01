import * as React from "react";
import { render } from 'react-dom';
import { Chart } from 'react-google-charts';
import * as axios from 'axios';

export interface HistogramProps {
	chartType: string;
	data?: Array<any>;
	options?: any;
	width?: string;
	chartEvents?: any;
	results?: any;
	update? : any;
	colors?: Array<String>
}

export class DSTHistogram extends React.Component <HistogramProps, undefined> {
	chartEvents: any;
	data: any;
	state: any;
	constructor(props: any){
		super(props);
	}
	render() {
		if( this.state && this.state.data ){
			return (
				<div className={'my-pretty-chart-container'}>
					<Chart
					chartType={this.props.chartType}
					data={this.state.data}
					options={this.props.options}
					graph_id="dst-histogram"
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
	 * 
	 * @memberof DSTHistogram
	 */
	componentDidMount(){
		const self = this;
        axios({
            method: 'post',
            url: 'https://pctf.herokuapp.com/main',
            data: {
                type: "initDST"
            }
        }).then( ( response: any ) => {
            const dbResults: Array<any> = [ [ "Destination Port", "Frequency" ] ];

            response.data.db.forEach( ( row: any ) => {
                // dbResults.push([ row.dst_port.toString(), parseInt(row.count) ]);
				dbResults.push([ row.dst_port, parseInt(row.count) ]);
            });
			self.data = dbResults;
			console.log( 'dbResults: ', dbResults );
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