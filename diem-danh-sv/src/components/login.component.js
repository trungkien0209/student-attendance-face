import React, { Component } from 'react'
import logo from "../assets/logo.png"

export default class Login extends Component {
    constructor(props) {
        super(props)
        this.state = {
            "email": "",
            "password": ""
        }
    }

    setParams = (event) => {
        this.setState({ [event.target.name]: event.target.value })
    }

    login = () => {
        var myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/x-www-form-urlencoded");

        var urlencoded = new URLSearchParams();
        urlencoded.append("email", this.state.email);
        urlencoded.append("password", this.state.password);

        var requestOptions = {
            method: 'POST',
            headers: myHeaders,
            body: urlencoded,
            redirect: 'follow'
        };

        fetch("http://127.0.0.1:5000/login", requestOptions)
            .then(response => {
                console.log(response)
                if (response.ok) {
                    return response.json()
                }
                throw Error(response.status)
            })
            .then(result => {
                console.log(result)
                window.localStorage.setItem("token", result.token)
                window.location.href = "./home"
            })
            .catch(error => {
                console.log('error', error)
                alert("Sai tên đăng nhập hoặc mật khẩu")
            }
            );
    }

    render() {
        return (
            <div className="login-wrapper">
                <div className="login-inner">
                    <div className='col-3'>
                        <img src={logo} />
                    </div>
                    <div className='content col-9'>
                        <h3>ĐĂNG NHẬP</h3>
                        <div className="mb-3">
                            <input type="email" className="form-control" name='email' onChange={this.setParams} placeholder="Nhập email" />
                        </div>
                        <div className="mb-3">
                            <input type="password" className="form-control" name='password' onChange={this.setParams} placeholder="Nhập mật khẩu" />
                        </div>
                        <div className="mb-3">
                            <div className="custom-control custom-checkbox">
                                <input
                                    type="checkbox"
                                    className="custom-control-input"
                                    id="customCheck1"
                                />
                                <label className="custom-control-label" htmlFor="customCheck1">
                                    Lưu tài khoản
                                </label>
                            </div>
                        </div>
                        <div className="d-grid">
                            <button type="button" className="btn btn-success" onClick={this.login}>ĐĂNG NHẬP</button>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}