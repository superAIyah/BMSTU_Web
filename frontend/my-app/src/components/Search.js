import React, {useContext, useEffect, useState, Fragment} from "react"
import { useParams} from "react-router-dom";
import axios from "axios";

import Breadcrumb from 'react-bootstrap/Breadcrumb';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import 'bootstrap/dist/css/bootstrap.min.css';
import {AuthContext} from "../context";
import Form from 'react-bootstrap/Form';
import Cookies from 'js-cookie';
import InputGroup from 'react-bootstrap/InputGroup';

export default function Search() {
    var searchText = window.localStorage.getItem('searchText')
    var minPrice = window.localStorage.getItem('minPrice')
    var maxPrice = window.localStorage.getItem('maxPrice')
    console.log(searchText)
    console.log(minPrice)
    console.log(maxPrice)

    const [data, setData] = useState([])
    async function fetchSubjects() {  // Using local server django rest api
        const response = await axios.get("/api/articles/?min_price="+minPrice+"&max_price="+maxPrice+"&text="+searchText)
        console.log(response.data)
        setData(response.data)
    }

    const [user, setUser] = useState([])
    async function getUser() {
        const config = {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': Cookies.get('csrftoken')
            }
        };

        const response = await axios.get("/api/user/", config)
        setUser(response.data.username)
    }
    
    
    useEffect( () => {
            console.log('effect')
            fetchSubjects()
            getUser() 
        }, []
    )

    async function handleBuy(article) {
        await axios.patch('/api/articles/'+article.id+'/', {
            "cart" : true
        })
    }

    const [edit, setEdit] = useState("")
    function handleEdit(article) {
        const config = {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': Cookies.get('csrftoken')
            }
        };

        axios.patch('/api/articles/'+article.id+'/', {
            "title" : edit
        }, config)
        console.log(101)
        console.log(edit)
        const ind = data.indexOf(article)
        const arr = data
        arr[ind].title = edit
        console.log(111)
        console.log(arr)
        setData([...arr])
    }

    function searchAdmin(article) {
        return (
            <Fragment>
            <InputGroup className="mb-3" style={{ width: "16.4rem", height: "1.3em"}}>
                <Form.Control
                    placeholder="Change title"
                    aria-label="Change title"
                    aria-describedby="basic-addon2"
                    onChange={e => setEdit(e.target.value)}
                    type="text"
                />
                <Button onClick={()=>handleEdit(article)} variant="outline-secondary" id="button-addon2">
                    Edit
                </Button>
            </InputGroup>
        </Fragment>
        )
    }

    function searchUser(article) {
        return (
            <Fragment>
            <Button variant="primary" onClick={()=>handleBuy()}>
                Buy this article
            </Button>
        </Fragment>
        )
    }

    return (
        <div>
            <center><h2>Results filtered by price from {minPrice} $ to {maxPrice} $ having text: {searchText}</h2></center>
            {data
                .map(article => {
                    return (
                        <Card style={{ width: '18rem' }}>
                            <Card.Img variant="top" src={article.photo_link} />
                            <Card.Body>
                                <Card.Title>
                                    <p><a href={article.link}>Demo version</a></p>
                                </Card.Title>
                                <Card.Text>
                                    {article.title}
                                </Card.Text>
                                <ListGroup.Item>{article.price} $</ListGroup.Item>
                                {user === "main" ? searchAdmin(article) : searchUser(article)}
                            </Card.Body>
                        </Card>
                    )
                })}
        </div>
    )
}