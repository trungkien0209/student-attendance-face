import React, { Component } from 'react'
import add from "../assets/add.png"

export default class Attendance extends Component {
    render() {
        return (
            <div>
                <div className='attendanceheader'>
                    <div className="row justify-content-between">
                        <div className="col-12">
                            <ul>
                                <li>
                                    <h3>ĐIỂM DANH SINH VIÊN</h3>
                                </li>
                                <li>
                                    <p><u>Thoát</u></p>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div className='attendancecontent'>
                    <div className="row justify-content-between">
                        <div className="form-group col-2">
                            <select className="form-control" id="exampleFormControlSelect1">
                                <option>10</option>
                                <option>20</option>
                                <option>50</option>
                                <option>100</option>
                                <option>Max</option>
                            </select>
                        </div>
                        <div class="col-2">
                            <img className='add' src={add} />
                        </div>
                    </div>
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th scope='col'>STT</th>
                                <th scope="col">Ngày điểm danh</th>
                                <th scope="col">Trạng thái</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <th scope="row">1</th>
                                <td>
                                    <h6>19/04/2023</h6>
                                    <p>9:00 - 9:30</p>
                                </td>
                                <td>2/3</td>
                            </tr>
                            <tr>
                                <th scope="row">2</th>
                                <td>
                                    <h6>19/04/2023</h6>
                                    <p>15:00 - 15:30</p>
                                </td>
                                <td>...</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        )
    }
}