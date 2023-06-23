import React, { Component } from 'react'
import { useParams } from 'react-router-dom'
import student from "../assets/student.png"
import facial_recognition from "../assets/facial_recognition.png"
import statistics from "../assets/statistics.png"
import search from "../assets/search.png"
import back from "../assets/back.png"
import { Link } from 'react-router-dom';

class Class extends Component {
    constructor(props) {
        super(props)
        this.state = {
            "data": {}
        }
    }

    back = () => {
        window.location.href = "/home"
    }

    componentDidMount() {
        this.loadDataClass()

    }
    loadDataClass = () => {
        var requestOptions = {
            method: 'GET',
            redirect: 'follow'
        };
        const { id } = this.props.params;
        fetch(`http://127.0.0.1:5000/classdetails/${id}`, requestOptions)
            .then(response => {
                if (response.ok) {
                    return response.json()
                }
                throw new Error(response.status)
            })
            .then(result => {
                console.log(result)
                this.setState({ data: result })
            })
            .catch(error => console.log('error', error));
    }
    render() {
        const { id } = this.props.params;
        return (
            <div>
                <div className='classheader'>
                    <div className="row justify-content-between">
                        <div className="col-3">
                            <ul className='header-title'>
                                <li>
                                    <h4>{this.state.data.class}</h4>
                                </li>
                                <li>
                                    <p>{this.state.data.coursre}</p>
                                </li>
                            </ul>
                        </div>
                        <div className='col-2'>
                            <ul className='header-tool'>
                            <p onClick={this.back}><u><img src={back} /></u></p>
                            </ul>
                        </div>
                    </div>
                </div>
                <div className='classcontent'>
                    <div className="row">
                        <div className="col-6 col-md-4">
                            
                                <div>
                                
                                    <ul>
                                    <Link to={`../studentclass/${id}`}>
                                        <li>
                                            <img src={student} />
                                        </li>
                                        </Link>
                                        <li>
                                            <span>Sinh viên</span>
                                        </li>
                                    </ul>
                                    
                                </div>
                           
                        </div>
                        <div className="col-6 col-md-4">
                            
                                <div>
                                    <ul>
                                        <Link to={`../statistic/${id}`}>
                                        <li>
                                            <img src={statistics} />
                                        </li>
                                        </Link>
                                        <li>
                                            <span>Thống kê</span>
                                        </li>
                                    </ul>
                                </div>
                            
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default (props) => (
    <Class
        {...props}
        params={useParams()}
    />
);