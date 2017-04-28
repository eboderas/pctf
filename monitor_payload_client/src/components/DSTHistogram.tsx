import * as React from "react";
import { render } from 'react-dom';
import { Chart } from 'react-google-charts';

export interface HistogramProps {
	chartType: string;
	data: Array<any>;
	options?: any;
	width?: string;
}

export class DSTHistogram extends React.Component <HistogramProps, undefined> {
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
        />
      </div>
    );
  }
}