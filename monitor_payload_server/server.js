const argv = require( 'yargs' ).argv,
	cors = require( 'cors' ),
	express = require( 'express' ),
	bodyParser = require( 'body-parser' ),
	path = require( 'path' );

const pool = require( path.join( __dirname, 'db', 'poolHandler' ) ),
	queryBuilder = require( path.join( __dirname, 'db', 'queryBuilder' ) );

let app = express();

app.use( cors() );
app.use( bodyParser.json() );

app.set( 'port', argv.port || 8080 );

app.get( '/', ( request, response ) => {
	response.send( 'hola' );
} );

app.post( '/main', ( request, response ) => {
	console.log( request.body );
	//if valid json
	pool.connect((err, client, done) => {
		if(err)
			return(console.log(`Error fethching client from pool ${err}`));
		//query here
		client.query( queryBuilder( request.body ), (err, result) => {
				done(err);

				if(err)
					console.log(`error running query ${err}`);

				console.log(result.rows);

				response.json( {
					data: result.rows
				} );
		} );
	});
} );

app.listen( app.get( 'port' ), () => {
	console.log( `server listening on port : ${app.get( 'port' )}` );
} );