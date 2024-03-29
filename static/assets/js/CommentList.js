//  delete once item in array

function removeItemOnce(arr, value) {
    var index = arr.indexOf(value);
    if (index > -1) {
        arr.splice(index, 1);
    }
    return arr;
}

// id
let id = 0
let ids = []

// buttons & elements
const checkallbtn = document.getElementById('All_Checked')
const runbtn = document.getElementById('runBtn')
const filterbtn = document.getElementById('filter')
const selectorinput = document.getElementById('selectRun')
const posts=document.getElementById('result_list_post')
const checkboxs=document.querySelectorAll('.new-control-input')
const myloader=document.querySelector('.my-loader')
// Set eventlistener
checkboxs.forEach(el=>el.addEventListener('click',()=>{togglecheck(event)}))
// Manage and switch between commands
class Selector {

    constructor() {
        runbtn.addEventListener('click', () => {
            this.swManage()
        })
        document.querySelectorAll('.posted_btn').forEach((el)=>{
        
            el.addEventListener('click',()=>{
                ids=[]
                ids.push(el.getAttribute('data-id'))
                draftOrpost('post')
            })
        })
        checkallbtn.addEventListener('click',()=>{
         
            if(checkallbtn.checked==true){
                ids=[]
                posts.querySelectorAll('tbody tr').forEach(el=>{
                        ids.push(el.getAttribute('data-field-number'))
                })
                oncheck(ids)    
            }else{
                offcheck(ids)
                ids=[]
            }
        })
    }
    swManage() {
       
        switch (selectorinput.value) {
            case 'delete':
                deleteItems.mulitidelete(ids)
                break;

            case 'draft':
                draftOrpost("draft")
                break;

            case 'post':
                draftOrpost("post")
                break;
            default:
                break;
        }
    }
}
new Selector()

// function for send request and doing commands
let mystatus=false
const draftOrpost = (key) => {
    if (mystatus == false && ids.length>0) {
        mystatus = true
        myloader.style.display = 'flex'
        var self = this;
        axios({
            method: 'post',
            url: url_draft,
            data: {
                id: ids,
                key:key
            },
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
                Accept: "application/json",
            }
        }).then(function (response) {
            if (response.data['status']) {
               if(key=='draft'){
                response.data['ids'].forEach(id=>{
                    posts.querySelector(`tbody tr[data-field-number='${id}'] td .badge`).parentElement.innerHTML='<span class="badge badge-danger">منتظر تایید</span>'
                })
               }else{
                  response.data['ids'].forEach(id=>{
                    posts.querySelector(`tbody tr[data-field-number='${id}'] td .badge`).parentElement.innerHTML='<span class="badge badge-success">منتشر شده</span>'
                })
               }
            }else{
                throw new Error("Custom Error Message");
            }
        }).catch(function (error) {
            myloader.style.display = 'none'
        }).finally(()=>{
            mystatus=false;
            offcheck(ids)
            myloader.style.display = 'none'

            ids=[]
        })
    }
}


// check
function oncheck(ids){
    ids.forEach(id => {
        posts.querySelector(`tbody tr[data-field-number='${id}'] .new-control-input`).checked=true
    });

}
// off check
function offcheck(ids){
    ids.forEach(id => {

        if(id!=null){
        posts.querySelector(`tbody tr[data-field-number='${id}'] .new-control-input`).checked=false}
    });
  
}

function togglecheck(e){
    let id=e.target.getAttribute('data-field-number')
    if(ids.includes(id)){
        removeItemOnce(ids,id)
    }else{
        ids.push(id)
     
    }
}

// delete item
class DeleteItem {
    //  properties
    status = false
    single=null
    backup=null
    ConfirmBtn = document.getElementById('btn_confirm_delete')
    AllElement = document.querySelectorAll("tr[data-field-number]")
    alldel=document.getElementById('allbtn')
    constructor() {
        this.AllElement.forEach((el) => {
            el.querySelector('.deleteBtn').addEventListener('click', () => {
                this.reset()
                this.getId(el.getAttribute('data-field-number'))
            })
        })
        this.ConfirmBtn.addEventListener('click', (e) => {
            if (!this.status) {
                this.ConfirmDeleted()
            }
        })
    }
    // methods
    getId(iid) {
        this.status = false
        this.backup = [Number(iid)]
    }

    mulitidelete(ids){
        if(ids.length>0){
        this.reset()
        this.alldel.click();
        this.backup=ids
        
    }}
    ConfirmDeleted() {
        if (this.status == false) {
            this.status = true
            this.ConfirmBtn.querySelector('span').style.display = 'none'
            this.ConfirmBtn.querySelector('svg').style.display = "block";
            var self = this;
            axios({
                method: 'post',
                url: myurl,
                data: {
                    id: this.backup,
                },
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    Accept: "application/json",
                }
            }).then(function (response) {
                console.log(response)
                if (response.data['status']) {
                    self.Finnish(response.data['ids'])  
                }else{
                    throw new Error("Custom Error Message");
                }
            }).catch(function (error) {
                self.ConfirmBtn.querySelector('span').innerHTML = "خطا در حذف، لطفا مجددا امتحان کنید."
                self.ConfirmBtn.querySelector('svg').style.display = 'none'
                self.ConfirmBtn.querySelector('span').style.display = 'block'

            }).finally(()=>{
                checkallbtn.checked=false
                this.status=false;
            })
        }
    }
    reset(){
  
            this.ConfirmBtn.classList.remove('btn-success')
            this.ConfirmBtn.classList.add('btn-danger')
            this.ConfirmBtn.querySelector('span').innerHTML = "حذف"
          
        
    }
    
    Finnish(items) {
   
        this.ConfirmBtn.querySelector('svg').style.display = "none";
        this.ConfirmBtn.classList.add('btn-success');
        this.ConfirmBtn.querySelector('span').style.display = 'block'
        this.ConfirmBtn.querySelector('span').innerHTML = "حذف شد!"
        items.forEach((it)=>{
            
            document.querySelector(`[data-field-number='${it}']`).remove()
        })
      ids=[]
    }
}
const deleteItems = new DeleteItem();

