import React, { Component } from 'react'
import complete from "../assets/complete.png"
import unfinished from "../assets/unfinished.png"
import DataTable from 'react-data-table-component'
import { useParams } from 'react-router-dom'
class Statistic extends Component {
    state = {
        data: [],
        isLoaded: false,
    }

    componentDidMount() {
        this.loadData()
    }

    back = () => {
        const { id } = this.props.params;
        window.location.href = `/class/${id}`
    }

    loadData = async() =>{
        try {
            const { id } = this.props.params;
            const response =await fetch(`http://127.0.0.1:5000/loadDataClass/${id}`);
            const data =await response.json();
            console.log(data);
            setTimeout(() => {
                this.setState({ data: data, isLoaded: true })
            }, 1000);
        } catch (err) {
            console.log(err)
        }
    }
    render() {
        const { data ,isLoaded} = this.state;
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
                name: "Ngày",
                selector: (row) => row.date
            },
            {
                name: "Giờ vào",
                selector: (row) => row.time
            },
        ]
        return (
            <div>
                <div className='statisticheader'>
                    <div className="row justify-content-between">
                        <div className="col-12">
                            <ul>
                                <li>
                                    <h3>THỐNG KÊ SINH VIÊN VÀO LỚP</h3>
                                </li>
                                <li>
                                <p onClick={this.back}><u>Thoát</u></p>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div className='statisticcontent'>
                <DataTable columns={columns} data={data} pagination fixedHeader fixedHeaderScrollHeight='579px'/>
                </div>
            </div>
        )
    }
}
export default (props) => (
    <Statistic
        {...props}
        params={useParams()}
    />
);