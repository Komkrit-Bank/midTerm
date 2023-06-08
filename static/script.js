const select_data = document.getElementById('search-dep')
const searchInput = document.querySelector('[data-search]')
const item_list = document.querySelectorAll('.console')

const onChange = () => {
    console.log(select_data.value)
}

searchInput.addEventListener('input', event => {
    const value = event.target.value
    item_list.forEach(item => {
        const isVisible = item.innerHTML.trim().toLowerCase().includes(value.toLowerCase())
        item.classList.toggle('hide', !isVisible)
    })
    console.log(item_list)
})

