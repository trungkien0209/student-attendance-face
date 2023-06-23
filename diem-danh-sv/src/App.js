import logo from './logo.svg';
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Login from './components/login.component'
import Home from './components/home.component'
import Class from './components/class.component'
import AddClass from './components/addclass.component'
import Student from './components/student.component'
import Statistic from './components/statistic.component'
import './App.css'
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'

function App() {
  return <BrowserRouter>
  <Routes>
    <Route path='/' element={<Login/>}/>
    <Route path='/home' element={<Home/>}/>
    <Route path='class/:id' element={<Class/>}/>
    <Route path='/addclass' element={<AddClass/>}/>
    <Route path='/studentclass/:id' element={<Student/>}/>
    <Route path='/statistic/:id' element={<Statistic/>}/>
  </Routes>
  </BrowserRouter>;
}

export default App;
