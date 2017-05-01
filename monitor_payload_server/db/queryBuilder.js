//sample query builder
const queryBuilder = ( filters ) => {
	if( filters.type === 'dst' ){
		return `SELECT src_port, dst_port, "timestamp", payload, id, length
	FROM public.payloads where dst_port=${ filters.results[0] } order by id desc limit 100;`;
	}
	else if( filters.type === 'payload' ){
		return `SELECT src_port, dst_port, "timestamp", payload, id, length
	FROM public.payloads where length=${ filters.results[0] } order by id desc limit 100;`;
	}
	else if( filters.type === 'initDST' ){
		return `SELECT A.dst_port, count(*)
	FROM (select * from public.payloads order by id desc limit 200) as A group by A.dst_port ;`;
	}
	else{
		return `SELECT A.length, count(*)
	FROM (select * from public.payloads order by id desc limit 200) as A group by A.length ;`;
	}
};

module.exports = queryBuilder;