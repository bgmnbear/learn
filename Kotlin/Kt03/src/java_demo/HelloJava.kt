package java_demo

import kotlin_demo.User

/**
 * Created by intel on 2018/3/15.
 */
object HelloJava {
    @JvmStatic fun main(args: Array<String>) {
        val user = User(0, "whister")
        println(user)
    }
}
