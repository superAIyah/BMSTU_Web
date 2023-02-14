import React, {useContext, useEffect, useState} from "react"
import { useParams} from "react-router-dom";
import axios from "axios";

import Breadcrumb from 'react-bootstrap/Breadcrumb';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import 'bootstrap/dist/css/bootstrap.min.css';
import {AuthContext} from "../context";
import Cookies from 'js-cookie';

export default function Articles() {
    const {isAuth, setIsAuth} = useContext(AuthContext);
    const {id} = useParams()

    const [data, setData] = useState([])
    async function fetchSubjects() {  // Using local server django rest api
        const response = await axios.get('/api/articles/')
        console.log(response.data)
        setData(response.data)
    }

    useEffect( () => {
            console.log('effect')
            fetchSubjects()
        }, []
    )

    async function handleClick(article) {
        const config = {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': Cookies.get('csrftoken')
            }
        };

        await axios.patch('/api/articles/'+article.id+'/', {
            "cart" : true
        }, config)
    }

    return (
        <div>
            <Breadcrumb>
                <Breadcrumb.Item href="/">Home</Breadcrumb.Item>
                <Breadcrumb.Item href="/subjects">
                    Library
                </Breadcrumb.Item>
                <Breadcrumb.Item active>{data.find(article => article.subject_id === +id)?.subject}</Breadcrumb.Item>
            </Breadcrumb>

            {data
                .filter(article => article.subject_id === +id)
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
                                <Button variant="primary" onClick={()=>handleClick(article)}>
                                    Buy this article
                                </Button>
                            </Card.Body>
                        </Card>
                    )
                })}
        </div>
    )
}