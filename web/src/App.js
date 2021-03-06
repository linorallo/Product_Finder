import React from 'react';
import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom';

//components
import './Assets/css/styles.min.css';
import './Assets/css/styles.css';
import Header from './components/headerComponents/header';
import Footer from './components/footerComponent/footer';
import Homepage from './components/pages/homePage';
import Products from './components/pages/products';
import Contact from './components/pages/contact';
import Search from './components/pages/search';

//includes
function App() {
  return (
    <Router>
      <div className="App">
        <Header/>
        <Route exact path='/' component={Homepage} />
        <Route exact path='/search' component={Search}/>
        <Route exact path='/Products' component={Products} />
        <Route exact path='/contact'component={Contact} />
        <Footer/>
      </div>
    </Router>
  );
}

export default App;
