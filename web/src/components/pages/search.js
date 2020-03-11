import React, {Component} from 'react';
import {Paper, Grid, ButtonBase, Typography, Button, withStyles, makeStyles, ListItemIcon} from '@material-ui/core';
import ResponsiveDrawer from '../side_drawer';

const StyledButton = withStyles({
    root:{
        fontSize:19,
    }
})(Button);

const useStyles = makeStyles(theme => ({
    margin: {
      margin: theme.spacing(1),
    },
}));

class Search extends Component{

    constructor(props){
        super(props)
        this.state ={
            itemList:[],
            isLoaded:false
        };
    }

    componentDidMount(){
        this.fetchData();
    }

///        .then(parsedJSON => console.log(parsedJSON.results))  para mostar resultados en consola
    fetchData(){
        console.log('http://localhost:5000/search/'+window.location.search.replace('?search=',''));
        fetch('http://localhost:5000/search/'+window.location.search.replace('?search=',''),{ mode: 'cors'})
        .then(response => response.json())

        .then(parsedJSON => parsedJSON.results.map(item => (
          {
            name: `${item.name}`,
            img: `${item.img}`,
            price: `${item.price}`,
            discount: `${item.discount}`,
            link: `https://${item.link}`
          }
        )))
        .then(itemList => this.setState({
          itemList, 
          isLoaded:true
        }))
        .catch(error => console.log('parsing failure', error))
        console.log(this.state.itemList)
    }
    basura(item){
        if(item.discount = 0){
            return<p>${item.price}</p>  ;
        }else{
            return<p>${item.price} | {item.discount}% off!</p>;
        }
    }
    showPrice(item){
        var item = this.props.obj
    return <p>en showPrice {item.price}</p>
        
    }


    

    render(){
        const {isLoaded, itemList} = this.state;
        return(
            <div className='container-fluid'>
                <div className=" m-1 mx-auto">
                    <form action="/search" method="get" onSubmit={this.handleSubmit} className="form-inline justify-content-center">
                        <div className="form-group">
                          <input type="text" id=""  className="form-control mb-2 mr-sm-2" onChange={this.handleChange} name="search" placeholder="What are you looking for?" value={this.state.searchString}/>
                        </div>
                        <input type="submit" className="btn btn-secondary mb-2" value="Search" />
                      </form>
                </div>


                <h3>   
                    Showing results for "{window.location.search.split('?search=')}"...
                </h3>
                <div className="row">
                    <div className="col-sm-">
                        <div className="container container-fluid">
                            <h4>Filter</h4>
                            <h5><li>Condition</li></h5>
                            <div className="form-check">
                                <input className="form-check-input" type="checkbox" value="" id="defaultCheck"/>
                                <label className="form-check-label" for="defaultCheck">New</label>
                            </div>
                            <div className="form-check">
                                <input className="form-check-input" type="checkbox" value="" id="defaultCheck"/>
                                <label className="form-check-label" for="defaultCheck">Refurbished</label>
                            </div>
                        </div>
                    </div>
                <div className="col-sm">
                    <table className='table-responsive-sm'>
                        <tbody>
                            <div>
                                {itemList.map(item =>( 
                                    <tr scope='row'>
                                        <Paper>
                                            <Grid container spacing={1}>
                                                <Grid item>
                                                    <ButtonBase>
                                                        <a href={item.link}>
                                                            <div id='img-cointainer'>
                                                                <img src={item.img} className="img-item" id='img-item'/>
                                                            </div>
                                                        </a>
                                                    </ButtonBase>
                                                </Grid>
                                                <Grid item xs={12} sm container>
                                                    <Grid item xs container direction='column' spacing={1}>
                                                        <Grid item xs>
                                                            <a href={item.link}>
                                                                <Typography gutterBottom variant='subtitle1'>
                                                                    {item.name}
                                                                </Typography>
                                                            </a>
                                                        </Grid>
                                                        <Grid item>

                                                            <Button variant='outlined' color='primary' > ${item.price}
                                                            </Button>
                                                            <span className="badge badge-success">{item.discount}% off</span>
                                                        </Grid>
                                                    </Grid>
                                                </Grid>
                                            </Grid>
                                        </Paper>
                                    </tr>
                                ))}
                            </div>
                        </tbody>
                    </table>  
                </div>
               </div> 
                <ul class="pagination justify-content-center">
                    <li class="page-item"><a class="page-link" href="#">Previous</a></li>
                    <li class="page-item"><a class="page-link" href="#">1</a></li>
                    <li class="page-item"><a class="page-link" href="#">2</a></li>
                    <li class="page-item"><a class="page-link" href="#">3</a></li>
                    <li class="page-item"><a class="page-link" href="#">Next</a></li>
                </ul> 
                    
            </div>
        )
    }
}

export default Search;