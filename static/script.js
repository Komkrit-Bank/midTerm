const select_data = document.getElementById('search-dep')
const searchInput = document.querySelector('[data-search]')
const item_list = document.querySelectorAll('.console')
const itemCardTemplate = document.querySelector('[data-show-template]')
const searchResult = document.querySelector('[search-result]')
const cardContainer = document.querySelector('[card-container]')

async function main(){
  await fetch("/product-list")
    .then(response => response.json())
    .then(data => {
      data.forEach(item => {
        const card = itemCardTemplate.content.cloneNode(true);
        const image = card.querySelector('[item-img]');
        const name = card.querySelector('[item-name]');
        const detail = card.querySelector('[item-detail]');
        const price = card.querySelector('[item-price]');
        const btn_cart = card.querySelector('[btn-cart]');
        const btn_detail = card.querySelector('[btn-detail]');
        image.src = `static/images/${item.product_img}`
        name.textContent = item.product_name;
        detail.textContent = item.product_detail;
        price.innerHTML = `<b>Price: </b>${item.product_price}<b>$</b>`;
        btn_cart.href = `/orderlist/${item.product_id}`
        btn_detail.href = `/product/${item.product_id}`
        cardContainer.appendChild(card)
      })
    })
  }

searchInput.addEventListener('input', event => {
    const value = event.target.value
    const button = document.getElementById('btn-search')
    if (value === ''){
      button.disabled = true
    }else {
      button.disabled = false
    }
})

main()