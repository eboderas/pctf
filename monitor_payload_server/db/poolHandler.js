const pg = require('pg');
require( 'pg-parse-float' )( pg );

const config = {
	user: 'viicslnyyexdxx',
	database: 'dau3slm4jue1qn',
	password: '301287f0b3bbdffd7fe9684487ebb483b11d0e608f7432500c2d508afa99e140',
	host: 'ec2-54-221-254-72.compute-1.amazonaws.com',
	port: 5432,
	max: 10,
	idleTimeoutMillis: 30000,
	ssl: true
};

const pool = new pg.Pool(config);

pool.on('error', (err, client) => {
	console.error('idle client error', err.message, err.stack);
});

module.exports.query = (text, values, callback) => {
	console.log(`Running query: ${text} | ${values}`);
	return(pool.query(text, values, callback));
};

module.exports.connect = (callback) => {
	return(pool.connect(callback));
};