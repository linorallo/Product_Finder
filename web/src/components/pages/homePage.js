import React, { Component } from 'react';
import {Route} from 'react-router-dom';
import Search from './search';

class Homepage extends Component{
  constructor(props){
    super(props);
    this.state = {
      itemList: [],
      isLoaded: false,
      searchString:'',
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    
  }

  componentDidMount(){
    this.fetchData();
  }

  ///.then(parsedJSON => console.log(parsedJSON.results))   para mostrar los resultados en consola
  fetchData(){
    fetch('http://localhost:5000/',{ mode: 'cors'})
    .then(response => response.json())
    
    .then(parsedJSON => parsedJSON.results.map(item => (
      {
        name: `${item.name}`,
        price: `${item.price}`,
        discount: `${item.discount}`,
        img: `${item.img}`,
        link: `https://${item.link}`
      }
    )))
    .then(itemList => this.setState({
      itemList,
      isLoaded: true
    }))
    .catch(error => console.log('parsing failure', error))
  }
 
  handleChange(event){
    this.setState({searchString: event.target.value});
    console.log(this.state.searchString)
  }

  handleSubmit(event){
    console.log(event)
    console.log(this.state.searchString)
    return(
      <Route  path='/search/{}' component={Search}/>
    )
    
    event.preventDefault();
  }

  render(){
    const {isLoaded, itemList} = this.state;
    if(!isLoaded){
      return <div>Loading...</div>
    }
    else{
      return(
        <section>
          <section id="cover" className="min-vh-100">
            <div id="cover-caption">
              <div className="container">
                <div className="row text-white">
                  <div className="col-xl-5 col-lg-6 col-md-8 col-sm-10 mx-auto text-center form p-4">
                    <h1 className=" display-4 py-2 text-truncate">Product Finder</h1>
                    <div className="px-2">
                      <form id="form-homepage" action="/search" method="get" onSubmit={this.handleSubmit} className="justify-content-center">
                        <div className="form-group">
                          <input type="text" id="desired" className="form-control" onChange={this.handleChange} name="search" placeholder="What are you looking for?" value={this.state.searchString}/>
                        </div>
                        <input type="submit" className="btn btn-secondary" value="Go" />
                      </form>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
          <div className="container container-fluid">

        <div className="row">
            {itemList.map(item =>(
              <div className="col-sm-4 py-3 px-lg-5 border bg-light">
                <p>{item.name}</p>
                <img src={item.img} id='img-item' />
                <p>${item.price} | {item.discount}% off!</p>
                <a  className="btn btn-secondary rounded-pill "  href={item.link} >Explore</a>
              </div>
              
            ))}
        
          <div className="table-responsive" >
            <table className="table table-sm table-hover">
              <thead>
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">Name</th>
                  <th scope="col">Price</th>
                  <th scope="col">Discount</th>
                </tr> 
              </thead>
            
              <tbody>
                {itemList.map(item =>(

                  <tr key= {item.link}>
                      <th scope="row">
                        <li></li>
                      </th>
                      <td>
                        <a href={item.link} className="">{item.name}</a>
                      </td>
                      <td>${item.price}</td>
                      <td>{item.discount}%</td>
                  </tr>
                ))};
              </tbody>
                <div className="w-100"></div>
            </table>
          </div>
        </div>
          </div> 
                     
        </section>
        
      )
    }
    
  }
}


export default Homepage;
