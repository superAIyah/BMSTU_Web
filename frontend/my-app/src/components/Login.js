import React, { useState } from 'react';
import { Navigate, Link } from 'react-router-dom';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Cookies from 'js-cookie';
import { login } from '../actions/auth';
import { connect } from 'react-redux';
import CSRFToken from './CSRFToken';

function Login({login}) {
    const [formData, setFormData] = useState({
        username: '',
        password: '',
        re_password: ''
    });

    const [accountCreated, setAccountCreated] = useState(false);

    const { username, password } = formData;

    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = e => {
        e.preventDefault();
        console.log(username)
        console.log(password)
        login(username, password);
    };

    return (

        <Form onSubmit={e => onSubmit(e)}
        style = {{marginLeft : "3em", marginRight: "5em"}}>
        <CSRFToken/>
        <h1>Sign into your account</h1>
        <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Label>Username</Form.Label>
            <Form.Control type="text" placeholder="Enter username" name = "username" onChange={e => onChange(e)}/>
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword" name = "password" onChange={e => onChange(e)}>
            <Form.Label>Password</Form.Label >
            <Form.Control type="password" placeholder="Password" name = "password" value={password} onChange={e => onChange(e)}/>
        </Form.Group>
        <Button variant="primary" type="submit">
            Login
        </Button>
        </Form>
  );
}

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});

export default connect(mapStateToProps, {login})(Login);