import * as React from "react";

interface resultProp {
	results: any;
	title: string;
	value: string;
};

export class Results extends React.Component<resultProp, resultProp> {
    constructor( props: any ){
        super( props );
		this.state = {
			results: props.results,
			title: props.title,
			value: props.value
		}
    }
    render() {
		return(
			<div className="results-wrapper">
				<div className="title">
					<span>{ this.props.title }</span><span>{ this.props.value }</span>
				</div>
				{
					this.props.results.map( ( val: any, i: number ) => {
						return <span key={i}>{val}</span>
					})
				}
			</div>
		);
    }
}