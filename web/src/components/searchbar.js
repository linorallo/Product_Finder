import React from 'react';
import SearchField from "react-search-field";


function SearchBar(){
    return(
        <div className="">
            <SearchField
                placeholder="Search..."
                onChange={onChange}
                searchText="This is initial search text"
                classNames="test-class"
            />
        </div>
    )
}

export default SearchBar;
