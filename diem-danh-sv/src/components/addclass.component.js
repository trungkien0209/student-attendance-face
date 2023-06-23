import React, { useEffect, useState, Component } from 'react'
import { Link } from 'react-router-dom';
import axios from "axios"
import logo from "../assets/logo.png"


export default class AddClass extends Component {
    constructor(props) {
        super(props)
        this.state = {
            "nameclass": "",
            "course": ""
        }
    }

    setParams = (event) => {
        this.setState({ [event.target.name]: event.target.value })
    }

    addclass = () => {
        var formdata = new FormData();
        formdata.append("nameclass", this.state.nameclass);
        formdata.append("course", this.state.course);

        var requestOptions = {
            method: 'POST',
            body: formdata,
            redirect: 'follow'
        };

        fetch("http://127.0.0.1:5000/addclass", requestOptions)
            .then(response => {
                console.log(response)
                if (response.ok) {
                    return response.json()
                }
                throw Error(response.status)
            })
            .then(result => {
                console.log(result)
                window.location.href = "./home"
            })
            .catch(error => {
                console.log('error', error)
                alert("Không thể thêm")
            });
    }
    render() {
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
                    </div>
                </div>
                <div className='homecontent'>
                    <div className='homecontent-addclass'>
                        <ul>
                            <li>
                                <div>
                                    <label htmlFor="nameclass">Tên lớp học</label>
                                    <div className="col-sm-10">
                                        <input className="form-control" id="nameclass" placeholder="Tên lớp học" name='nameclass' onChange={this.setParams} />
                                    </div>
                                    <label htmlFor="course">Kỳ học</label>
                                    <div className="col-sm-10">
                                        <input className="form-control" id="course" placeholder="Kỳ học" name='course' onChange={this.setParams} />
                                    </div>
                                    <button onClick={this.addclass}>Thêm</button>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        )
    }
}