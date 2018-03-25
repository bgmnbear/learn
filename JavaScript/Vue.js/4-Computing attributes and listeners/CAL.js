var vm1 = new Vue({
    el: '#bad_example',
    data: {
        message: 'This is a game.',
    }
})

var vm2 = new Vue({
    el: '#example',
    data: {
        message: 'Hello'
    },
    computed: {
        // 计算属性的 getter
        reversedMessage: function () {
            // `this` 指向 vm 实例
            return this.message.split('').reverse().join('')
        },
        now: function () {
            return Date.now()
        },
    },
    methods: {
        reversedMessage: function () {
            return this.message.split('').reverse().join('')
        },
    },
})

var vm3 = new Vue({
    el: '#demo',
    data: {
        firstName: 'Foo',
        lastName: 'Bar'
    },
    computed: {
        fullName: {
            // getter
            get: function () {
                return this.firstName + ' ' + this.lastName
            },
            // setter
            set: function (newValue) {
                var names = newValue.split(' ')
                this.firstName = names[0]
                this.lastName = names[names.length - 1]
            }
        }
    }
})