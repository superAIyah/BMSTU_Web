import React, {useEffect, useState} from "react"
import axios from "axios";
import ListGroup from 'react-bootstrap/ListGroup';

export default function Subjects(){

    const [data, setData] = useState([])
    async function fetchSubjects() {
        const response = await axios.get('/api/subjects/')
        console.log(response.data)
        setData(response.data)
    }

    useEffect( () => {
            console.log('effect')
            fetchSubjects()
        }, []
    )

    return(
        <div>
            <ListGroup defaultActiveKey="#link1">
                <ListGroup.Item action href="/subjects/1">
                    {data[0]?.name}
                </ListGroup.Item>
                <ListGroup.Item action href="/subjects/2">
                    {data[1]?.name}
                </ListGroup.Item>
                <ListGroup.Item action href="/subjects/3">
                    {data[2]?.name}
                </ListGroup.Item>
            </ListGroup>
        </div>
    )

}