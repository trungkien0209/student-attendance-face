import React, { Component, useState, useEffect } from 'react'
import { MDBTable, MDBTableHead, MDBTableBody, MDBRow, MDBCol, MDBContainer, MDBBtn, MDBBtnGroup, MDBPagination, MDBAccordionItem, MDBPaginationLink } from "mdb-react-ui-kit"
import edit from "../assets/edit.png"
import del from "../assets/delete.png"
import search from "../assets/search.png"
import add from "../assets/add.png"
import axios from 'axios'
import { useParams } from 'react-router-dom'
import DataTable from 'react-data-table-component'

class Student extends Component {
    state = {
        data: [],
        dataStdClass: [],
        isLoaded: false,
        mssv: null,
        delmssv:null,

    }

    componentDidMount() {
        this.loadDataStd()
        this.loadDataStdClass()
    }



    loadDataStd = async() =>{
        try {
            const response =await fetch('http://127.0.0.1:5000/sv');
            const data =await response.json();
            console.log(data);
            setTimeout(() => {
                this.setState({ data: data, isLoaded: true })
            }, 1000);
        } catch (err) {
            console.log(err)
        }
    }

    loadDataStdClass = async() =>{
        try {
            const { id } = this.props.params;
            const response =await fetch(`http://127.0.0.1:5000/studentclass/${id}`);
            const dataStdClass =await response.json();
            console.log(dataStdClass);
            setTimeout(() => {
                this.setState({ dataStdClass: dataStdClass, isLoaded: true })
            }, 1000);
        } catch (err) {
            console.log(err)
        }
    }

    addStdClass = () => {
        var formdata = new FormData();
        formdata.append("mssv", this.state.mssv);
        const { id } = this.props.params;
        var requestOptions = {
            method: 'POST',
            body: formdata,
            redirect: 'follow'
        };

        fetch(`http://127.0.0.1:5000/addstudentclass/${id}`, requestOptions)
            .then(response => {
                console.log(response)
                if (response.ok) {
                    return response.json()
                }
                throw Error(response.status)
            })
            .then(result => {
                console.log(result)
                window.location.reload();
            })
            .catch(error => {
                console.log('error', error)
                alert("Không thể thêm")
            });
    }

    deleteStdClass = () => {
        const id = this.state.delmssv;

        var requestOptions = {
            method: 'GET',
            redirect: 'follow'
        };

        
        fetch(`http://127.0.0.1:5000/deleteStdClass/${id}`, requestOptions)
        .then(response => {
            if(response.ok){
                return response.json()
            }
            throw new Error(response.status)
        })
        .then(result => {
            console.log(result)
            window.location.reload();
        })
        .catch(error => console.log('error', error));
    }
    back = () => {
        const { id } = this.props.params;
        window.location.href = `/class/${id}`
    }
    render() {
        const { data, dataStdClass  ,isLoaded} = this.state;

        const columns = [
        {
            name: "MSSV",
            selector: (row) => row.mssv,
        },
        {
            name: "Họ và tên",
            selector: (row) => row.name
        },
        {
            name: "Lớp",
            selector: (row) => row.class
        },
        {
            name: "Email",
            selector: (row) => row.email
        },
        {
            name: "Công cụ",
            cell: (row) =><button onMouseOver={() => this.setState({ ["mssv"]: row.mssv })} onClick={this.addStdClass}><img width={30} height={30} src={add}/></button>
        },
    ]
    const columnstd = [
        {
            name: "MSSV",
            selector: (row) => row.mssv,
            sortable: true
        },
        {
            name: "Họ và tên",
            selector: (row) => row.name,
            sortable: true
        },
        {
            name: "Lớp",
            selector: (row) => row.class,
            sortable: true
        },
        {
            name: "Email",
            selector: (row) => row.email
        },
        {
            name: "Công cụ",
            cell: (row) =><button onMouseOver={() => this.setState({ ["delmssv"]: row.id })} onClick={this.deleteStdClass}><img width={30} height={30} src={del}/></button>
        },
    ]
        return (
            <div className='studentall'>
                <div className='studentheader'>
                    <div className="row justify-content-between">
                        <div className="col-4">
                            <h3>QUẢN LÝ SINH VIÊN</h3>
                        </div>
                        <div className='col-6'>

                        </div>
                        <div className='col-2'>
                            <p onClick={this.back}><u>Thoát</u></p>
                        </div>
                    </div>
                </div>
                <div className='studentcontent'>
                    <DataTable columns={columnstd} data={dataStdClass} pagination fixedHeader fixedHeaderScrollHeight='179px'/>
                    <h1>Thêm sinh viên vào lớp</h1>
                    <DataTable columns={columns} data={data} pagination fixedHeader fixedHeaderScrollHeight='179px'/>
                </div>
            </div>
        )
    }
}
export default (props) => (
    <Student
        {...props}
        params={useParams()}
    />
);