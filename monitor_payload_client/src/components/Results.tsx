import * as React from "react";

interface resultProp {
	results: any;
};

export class Results extends React.Component<resultProp, resultProp> {
    constructor( props: any ){
        super( props );
		this.state = {
			results: props.results
		}
    }
    render() {
		return(
			<div className="results-wrapper">
				{
					this.props.results.map( ( val: any, i: number ) => {
						return <span key={i}>{val}</span>
					})
				}
			</div>
		);
    }
}