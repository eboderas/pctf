const expect = require('chai').expect;
const queryBuilder = require( '../db/queryBuilder' );


describe('queryBuilder test suite', () => {
	it('sample test', () => {
		expect(2 + 2).to.be.equal(4);
	});

	it( 'query builder', () => {
		const case1 = {},
		case2 = {},
		case3 = {},
		case4 = {},
		case5 = {},
		case6 = {},
		case7 = {},
		case8 = {};

		expect( queryBuilder( case1 ) ).to.be.equal( '' );

		expect( queryBuilder( case2 ) ).to.be.equal( '' );

		expect( queryBuilder( case3 ) ).to.be.equal( '' );

		expect( queryBuilder( case4 ) ).to.be.equal( '' );

		expect( queryBuilder( case5 ) ).to.be.equal( '' );

		expect( queryBuilder( case6 ) ).to.be.equal( '' );

		expect( queryBuilder( case7 ) ).to.be.equal( '' );

		expect( queryBuilder( case8 ) ).to.be.equal( '' );
	} );
});