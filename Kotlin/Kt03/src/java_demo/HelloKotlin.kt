package java_demo

import kotlin_demo.User

/**
 * Created by intel on 2018/3/15.
 */

fun main(args: Array<String>) {
    val user = User(0, "whister")
    println(user)
    HelloKotlin::class.constructors.map(::println)
}

class HelloKotlin {
    fun hello() {

    }
}