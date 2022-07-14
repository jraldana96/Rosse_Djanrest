var loginForm = document.getElementById('login')
var searchForm = document.getElementById('search-form')

var contentContainer = document.getElementById('content-container')

var baseEndpoint = "http://localhost:8000/api"
if (loginForm){
    loginForm.addEventListener('submit', handleLogin)
}
if (searchForm){
    searchForm.addEventListener('submit', handleSearch)
}


function handleLogin(event){
    event.preventDefault()

    let loginFormData = new FormData(loginForm) // get data from a form
    let loginObjectData = Object.fromEntries(loginFormData)
    //console.log(loginObjectData['username'])
    let bodyStr = JSON.stringify(loginObjectData)

    const loginEndpoint = `${baseEndpoint}/token/`
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: bodyStr
    }

    fetch(loginEndpoint, options)
    .then(response => {
        return response.json()
    })
    .then( authData =>{
        handleAuthData(authData, getProductList)
    }) 
    .catch(err => {
        console.log('error', err)
    })
}




function handleSearch(event){
    event.preventDefault()

    let formData = new FormData(searchForm) // get data from a form
    let data = Object.fromEntries(formData)

    let searchParams = new URLSearchParams(data)

    const endpoint = `${baseEndpoint}/search/?${searchParams}`
    const headers = {
        "Content-Type": "application/json"
    }
    const authToken = localStorage.getItem('access')
    if( authToken){
        headers['Authorization'] = `Beares ${authToken}`
    }
    const options = {
        method: "GET",
        headers: headers
    }

    fetch(endpoint, options)
    .then(response => {
        return response.json()
    })
    .then( data =>{
        console.log(data.hits)
        writeToContainer(data)
    }) 
    .catch(err => {
        console.log('error', err)
    })
}



function handleAuthData(authData, callback){
    localStorage.setItem('access',authData.access)
    localStorage.setItem('refresh',authData.refresh)

    if(callback){
        callback()
    }
}


function getFetchOptions(method, body){
    return options = {
        method: method === null ? "GET" : method,
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem('access')}`
        },
        //body: jsObject ? JSON.stringify(jsObject) : null
        body: body ? body : null
    }

}

function isTokenNotValid(jsonData){
    if(jsonData.code && jsonData.code === "token_not_valid"){
        // run a refresh token fetch.
        alert("please login again")
        return false
    }

    return true
}

function getProductList(){
    const endpoint = `${baseEndpoint}/productos/`
    const options = getFetchOptions()

    fetch(endpoint,options)
    .then(response=>{
        //console.log(response)
        return response.json()
    })
    .then(data=>{
        const validData = isTokenNotValid(data)
        if (validData){
            writeToContainer(data)
        }
    })

}

function validateJWTToken(){
    const endpoint = `${baseEndpoint}/token/verify/`
    const options = {
        method: "POST",
        headers: {
            "Content-Type":"application/json"
        },
        body: JSON.stringify({
            token: localStorage.getItem('access')
        })
    }
    fetch(endpoint, options)
    .then(response=>response.json())
    .then(x=>{

        // REFRESH

        // OR RELOGIN
        console.log(x)
        isTokenNotValid(x)
    })

}


function writeToContainer(data){
    if(contentContainer){
        contentContainer.innerHTML = "<pre>" + JSON.stringify(data, null, 4) + "</pre>"
    }
}

validateJWTToken()
//getProductList()