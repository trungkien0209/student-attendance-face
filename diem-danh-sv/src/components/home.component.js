import React, { useEffect, useState, Component } from 'react'
import { Link } from 'react-router-dom';
import axios from "axios"
import logo from "../assets/logo.png"
import logout from "../assets/logout.png"
import add from "../assets/add.png"
import xoa from "../assets/delete.png"

export default class Home extends Component {
    logout = () => {
        window.localStorage.removeItem("token")
        window.location.href = "./"
    }

    addclass = () => {
        window.location.href = "./addclass"
    }

    
    state = {
        data: [],
        isLoaded: false
    }

    async componentDidMount() {
        try {
            const response = await fetch('http://127.0.0.1:5000/class');
            const data = await response.json();
            console.log(data);
            setTimeout(() => {
                this.setState({ data: data.splice(0, 10), isLoaded: true })
            }, 1000);
        } catch (err) {
            console.log(err)
        }
    }

    render() {
        const { data, isLoaded } = this.state;
        const deleteclass = (id) => {
            var requestOptions = {
                method: 'GET',
                redirect: 'follow'
            };
    
            fetch(`http://127.0.0.1:5000/deleteClass/${id}`, requestOptions)
            .then(response => {
                if(response.ok){
                    return response.json()
                }
                throw new Error(response.status)
            })
            .then(result => {
                console.log(result)
                window.location.href = "./home"
            })
            .catch(error => console.log('error', error));
        }
        return (
            <div>
                <div className='homeheader'>
                    <div className="row justify-content-between">
                        <div className="header-title col">
                            <ul className='header-title'>
                                <li>
                                    <img src={logo} />
                                </li>
                                <li>
                                    <h3>HỆ THỐNG ĐIỂM DANH SINH VIÊN</h3>
                                </li>
                            </ul>
                        </div>
                        <div className="col-2">
                            <ul className='header-tool'>
                                <li onClick={this.addclass}>
                                    <img src={add} />
                                </li>
                                <li onClick={this.logout}>
                                    <span>Đăng xuất</span>
                                    <img src={logout} alt='' />
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div className='homecontent'>
                    {!isLoaded ? <div>Loading...</div> :
                        <div>
                            {
                                data.map((item, index) => (
                                    <div className='homecontent-class' key={index}>
                                        <ul>
                                            <li>
                                                <div>
                                                    <h5>{item.class}</h5>
                                                    <span>{item.coursre}</span>
                                                </div>
                                            </li>
                                            <div className='link'>
                                                <li>
                                                    <Link to={`../class/${item.id}`} className='btn btn-primary'>Quản lý</Link>
                                                </li>
                                            </div>
                                            <div className='deleteclass'>
                                                <li onClick={()=>deleteclass(`${item.id}`)}>
                                                    <img src={xoa} />
                                                </li>
                                            </div>
                                        </ul>

                                    </div>
                                ))
                            }
                        </div>
                    }
                </div>
            </div>
        )
    }
}