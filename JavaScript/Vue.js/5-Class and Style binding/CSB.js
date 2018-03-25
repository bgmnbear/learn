var vm = new Vue({
    el: '#example',
    data: {
        isActive: true,
        hasError: false,
    }
})

var vm1 = new Vue({
    el: '#example1',
    data: {
        classObject: {
            active: true,
            'text-danger': false,
        }
    }
})

var vm2 = new Vue({
    el: '#example2',
    data: {
        isActive: true,
        error: null,
    },
    computed: {
        classObject: function () {
            return {
                active: this.isActive && !this.error,
                'text-danger': this.error && this.error.type === 'fatal',
            }
        }
    }
})

var vm3 = new Vue({
    el: '#list',
    data: {
        activeClass: 'active',
        errorClass: 'text-danger',
    }
})

var vm4 = new Vue({
    el: '#inline-obj',
    data: {
        activeColor: 'red',
        fontSize: 30,
    }
})

var vm5 = new Vue({
    el: '#inline-obj1',
    data: {
        styleObject: {
            color: 'red',
            fontSize: '13px',
        }
    }
})

var vm6 = new Vue({
    el: '#inline-list',
    data: {
        baseStyles: {
            color: 'red',
            fontSize: '13px',
        },
        overridingStyles: {
            margin: 'auto',
        },
    }
})
