import React, { useState } from 'react';
import { Navigate, Link } from 'react-router-dom';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Cookies from 'js-cookie';
import { register } from '../actions/auth';
import { connect } from 'react-redux';
import CSRFToken from './CSRFToken';

function Register({register, isAuthenticated}) {
    const [formData, setFormData] = useState({
        username: '',
        password: '',
        re_password: ''
    });

    const [accountCreated, setAccountCreated] = useState(false);

    const { username, password, re_password } = formData;

    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = e => {
        e.preventDefault();

        if (password === re_password) {
            console.log("REGISTER")
            register(username, password, re_password);
            setAccountCreated(true);
        }
    };

    if (accountCreated)
        return <Navigate to='/login' />;

    return (

        <Form onSubmit={e => onSubmit(e)}
        style = {{marginLeft : "3em", marginRight: "5em"}}>
        <CSRFToken/>
        <h1>Register for an Account</h1>
        <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Label>Username</Form.Label>
            <Form.Control type="text" placeholder="Enter username" name = "username" value={username} onChange={e => onChange(e)}/>
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
            <Form.Label>Password</Form.Label>
            <Form.Control type="password" placeholder="Password" name = "password" value={password} onChange={e => onChange(e)}/>
        </Form.Group>
        <Form.Group className="mb-3" controlId="formBasicRePassword">
            <Form.Label>Confirm password</Form.Label>
            <Form.Control type="password" placeholder="Password"  name = "re_password" value={re_password} onChange={e => onChange(e)}/>
        </Form.Group>
        <Button variant="primary" type="submit">
            Register
        </Button>
        </Form>
  );
}

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});

export default connect(mapStateToProps, {register})(Register);