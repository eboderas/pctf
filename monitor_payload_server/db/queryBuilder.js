//sample query builder
const queryBuilder = ( filters ) => {
	return `select countryname, ${getColumn( filters.filter )}, countrycode, ${getColumn( filters.filter )}_color as color from pivot_indicators where year = ${filters.year} order by ${getColumn( filters.filter )}`;
};

const getColumn = ( field ) => {
	switch( field ){
		case 'GDP':
			return 'gdp_us';
		case 'FSI':
			return 'fsi';
		case 'INF':
			return 'inflation';
		case 'POP':
			return 'populationgrowth';
		case 'EMP':
			return 'employmentratio';
		case 'RES':
			return 'reserves';
		case 'FDI':
			return 'fdi';
		case 'TRA':
			return 'trade';
		default:
			return 'fsi';
	};
}

module.exports = queryBuilder;