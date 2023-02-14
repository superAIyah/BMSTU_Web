import React, { useEffect, Fragment } from 'react';
import { connect } from 'react-redux';
import { checkAuthenticated } from '../actions/auth';

const Layout = ({ children, checkAuthenticated }) => {
    useEffect(() => {
        checkAuthenticated();
    }, []);

    return (
        <Fragment>
            <p>a</p>
        </Fragment>
    );
};

export default connect(null, { checkAuthenticated })(Layout);