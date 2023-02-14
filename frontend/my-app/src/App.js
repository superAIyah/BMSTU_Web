import React, {useEffect, useState, Fragment } from "react"
import './App.css';
import { BrowserRouter, Route, Link, Routes } from "react-router-dom";
import Home from "./components/Home";
import Subjects from "./components/Subjects";
import Articles from "./components/Articles";
import Login from "./components/Login"
import Cart from "./components/Cart";
import Search from "./components/Search";
import ListGroup from "react-bootstrap/ListGroup";
import {AuthContext} from "./context/index"
import Button from "react-bootstrap/Button";
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import MultiRangeSlider from "./components/multiRangeSlider/MultiRangeSlider";
import Register from "./components/Register"
import axios from "axios";
import { Provider } from 'react-redux';
import store from './store';
import { connect } from 'react-redux';
import { logout } from './actions/auth';
import { checkAuthenticated } from "./actions/auth";
import Layout from './hocs/Layout';

function App({isAuthenticated, logout, checkAuthenticated}) {
    useEffect(() => {
        checkAuthenticated();
        console.log(111100005000)
    }, []);

    const  [isAuth, setIsAuth] = useState(false);

    // Cart state cmponents
    const [data, setData] = useState([])
    const [sum, setSum] = useState(0)

    async function handleOut() {
        const response = await axios.get('/api/articles/')
        const data = response.data
        for (const article of data) {
            if (article.cart === true) {
                axios.patch('/api/articles/'+article.id+'/', {
                    "cart" : false
                })
                article.cart = false;
            }
            console.log(data)
        }
        setData([...data])
        setSum(0)
        logout()
        
    }

    const [minPrice, setMinPrice] = useState(0)
    const [maxPrice, setMaxPrice] = useState(500)
    const [searchText, setSearchText] = useState("")

    function onSliderChange(min, max) {
        setMinPrice(min)
        setMaxPrice(max)
    }

    function onSearch() {
        window.localStorage.setItem('minPrice', minPrice);
        window.localStorage.setItem('maxPrice', maxPrice);
        window.localStorage.setItem('searchText', searchText);

        console.log(JSON.parse(window.localStorage.getItem('maxPrice')))
    }

    const guestLinks = (
        <Fragment>
            <Button href="/register"
                    style={{ width: "25rem", height: "3.5rem", marginLeft: 5, marginTop: 3, lineHeight: "2.5em"}}
            >
                Register
            </Button>
            <Button href="/login"
                    style={{ width: "25rem", height: "3.5rem", marginLeft: 5, marginTop: 3, lineHeight: "2.5em", marginRight: 5}}
            >
                Login
            </Button>
        </Fragment>
    );

    const authLinks = (
        <Fragment>
            <Button style={{ width: "25rem", height: "3.5rem", marginLeft: 5, marginTop: 3}}
                    onClick={()=>handleOut()}
            >
                Logout
            </Button>
            <Button
                action href="/cart"
                style={{ width: "15rem", height: "3.5rem", marginLeft: 5, marginRight: 5, marginTop: 3}}
                variant="outline-primary"
            >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 576 512"
                    fill="currentColor"
                >
                    <path d="M96 0C107.5 0 117.4 8.19 119.6 19.51L121.1 32H541.8C562.1 32 578.3 52.25 572.6 72.66L518.6 264.7C514.7 278.5 502.1 288 487.8 288H170.7L179.9 336H488C501.3 336 512 346.7 512 360C512 373.3 501.3 384 488 384H159.1C148.5 384 138.6 375.8 136.4 364.5L76.14 48H24C10.75 48 0 37.25 0 24C0 10.75 10.75 0 24 0H96zM128 464C128 437.5 149.5 416 176 416C202.5 416 224 437.5 224 464C224 490.5 202.5 512 176 512C149.5 512 128 490.5 128 464zM512 464C512 490.5 490.5 512 464 512C437.5 512 416 490.5 416 464C416 437.5 437.5 416 464 416C490.5 416 512 437.5 512 464z" />
                </svg>
            </Button>
        </Fragment>
    );

    return (
        <Provider store={store}>
            <AuthContext.Provider value = {{
                isAuth,
                setIsAuth
            }}>
                {/* <Layout> */}
                <BrowserRouter basename="/" >
                <div>
                    <ListGroup horizontal>
                        <ListGroup.Item action href="/">
                            Start
                        </ListGroup.Item>
                        <ListGroup.Item action href="/subjects">
                            Subjects
                        </ListGroup.Item>
                        <ListGroup.Item>
                        <MultiRangeSlider style={{maxheight: "1rem"}}
                            min={0}
                            max={500}
                            onChange={({ min, max }) => onSliderChange(min, max)}
                        />
                        </ListGroup.Item>
                        <ListGroup.Item>
                        <InputGroup className="mb-3" style={{ width: "25rem", height: "1.3em"}}>
                            <Form.Control
                                placeholder="Search by title"
                                aria-label="Search by title"
                                aria-describedby="basic-addon2"
                                onChange={e => setSearchText(e.target.value)}
                                type="text"
                            />
                            <Button onClick={()=>onSearch()} action href="/search" variant="outline-secondary" id="button-addon2">
                                Filter search
                            </Button>
                        </InputGroup>
                        </ListGroup.Item>
                        {isAuthenticated ? authLinks : guestLinks }
                            </ListGroup>
                    <hr />
                    <Routes>
                    <Route exact path="/" element={<Home />}>
                    </Route>
                        <Route exact path="/subjects" element={<Subjects />}>
                        </Route>
                        <Route exact path="/subjects/:id" element={<Articles />}>
                        </Route>
                        <Route exact path="/search" element={<Search
                            minPrice={minPrice}
                            maxPrice={maxPrice}
                            searchText={searchText}
                        />}>
                        </Route>
                        <Route exact path="/login" element={<Login />}>
                        </Route>
                        <Route exact path="/register" element={<Register />}>
                        </Route>
                        <Route exact path="/cart" element={<Cart 
                            data={data}
                            setData={setData}
                            sum={sum}
                            setSum={setSum}
                        />}>
                        </Route>
                    </Routes>
                </div>
                </BrowserRouter>
                {/* </Layout> */}
            </AuthContext.Provider>
        </Provider>
    );
  }

  const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});
export default connect(mapStateToProps, { logout, checkAuthenticated })(App);




